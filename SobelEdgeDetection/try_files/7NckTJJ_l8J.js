/*1357526526,173213725*/

if (self.CavalryLogger) { CavalryLogger.start_js(["Rs18G"]); }

__d("legacy:PhotoSnowlift",["PhotoSnowlift"],function(a,b,c,d){a.PhotoSnowlift=b('PhotoSnowlift');},3);
__d("PhotoViewerFollow",["Event","Arbiter","AsyncRequest","BanzaiODS","CSS","DOM","Parent","PhotosConst","$","copyProperties"],function(a,b,c,d,e,f){var g=b('Event'),h=b('Arbiter'),i=b('AsyncRequest'),j=b('BanzaiODS'),k=b('CSS'),l=b('DOM'),m=b('Parent'),n=b('PhotosConst'),o=b('$'),p=b('copyProperties');function q(s){this.viewer=s;}var r={};p(q,{createInstance:function(s,t,u,v,w,x,y,z){var aa=s.getInstance(),ba=new q(aa);ba.init(o(t),u,v,w,x,y,z);r[aa.getVersionConst()]=ba;return ba;},getInstance:function(s){return r[s];}});p(q.prototype,{FOLLOW_LOCATION_PHOTO:48,init:function(s,t,u,v,w,x,y){this.subscribeLink=s;this.unsubscribeFlyout=t;this.subscribeEndpoints=w;this.unsubscribeEndpoints=x;this.unsubLinks=v;this.unsubDiv=u;this.reset();this.activate();this.type=y;g.listen(this.subscribeLink,'click',function(event){if(m.byClass(event.getTarget(),'photoViewerFollowLink'))this.subscribePhotoOwner();}.bind(this));g.listen(this.unsubLinks.user,'click',this.unsubscribePhotoOwner.bind(this));g.listen(this.unsubLinks.page,'click',this.unsubscribePhotoOwner.bind(this));h.subscribe(['FollowUser','FollowUserFail','UnfollowUser','UnfollowUserFail'],this.updateSubscribe.bind(this));h.subscribe(this.viewer.getEventString('DATA_CHANGE'),this.showSubscribeLinkOnChange.bind(this));if(this.viewer.getVersionConst()===n.VIEWER_SNOWLIFT){h.subscribe(this.viewer.getEventString('CLOSE'),this.reset.bind(this));h.subscribe(this.viewer.getEventString('OPEN'),this.activate.bind(this));}this.registerUnsubscribeTarget();},activate:function(){this.activated=true;},reset:function(){this.unsubscribeFlyout&&this.unsubscribeFlyout.clearNodes();this.subscriptionChange={};this.activated=false;},registerUnsubscribeTarget:function(){if(!this.unsubscribeFlyout)return;var s=l.scry(this.subscribeLink,'.photoViewerFollowedMsg')[0];if(s&&!k.hasClass(s,'unsubFlyoutEnabled')){this.unsubscribeFlyout.initNode(s);k.addClass(s,'unsubFlyoutEnabled');}},updateSubscribe:function(s,t){if(!this.activated)return;var u=t.profile_id;if(u){this.subscriptionChange[u]=s==='FollowUser'||s==='UnfollowUserFail'?'following':'unfollowed';this.toggleSubscribeLink(u);}},showSubscribeLinkOnChange:function(s,t){this.type=t.ownertype;k.conditionClass(this.unsubDiv,'isPage',this.type==='page');this.toggleSubscribeLink(t.owner);},toggleSubscribeLink:function(s){var t=l.scry(this.subscribeLink,'span.fbPhotoSubscribeWrapper')[0];if(!t)return;if(this.subscriptionChange[s]){k.conditionClass(t,'followingOwner',this.subscriptionChange[s]==='following');if(this.subscriptionChange[s]==='unfollowed')this.unsubscribeFlyout&&this.unsubscribeFlyout.hideFlyout(true);}this.registerUnsubscribeTarget();},subscribePhotoOwner:function(){if(!this.viewer.getOwnerId())return;var s=(this.type==='user')?{profile_id:this.viewer.getOwnerId()}:{fbpage_id:this.viewer.getOwnerId(),add:true,reload:false,fan_origin:'photo_snowlift'};h.inform('FollowUser',{profile_id:this.viewer.getOwnerId()});if(this.type==='page')j.bumpEntityKey('snowlift_page_like','snowlift_page_like.clicked_link');s.location=this.FOLLOW_LOCATION_PHOTO;new i(this.subscribeEndpoints[this.type]).setAllowCrossPageTransition(true).setData(s).setMethod('POST').setReadOnly(false).setErrorHandler(h.inform.curry('FollowUserFail',s)).send();},unsubscribePhotoOwner:function(){if(!this.viewer.getOwnerId())return;var s=(this.type==='user')?{profile_id:this.viewer.getOwnerId()}:{fbpage_id:this.viewer.getOwnerId(),add:false,reload:false};h.inform('UnfollowUser',{profile_id:this.viewer.getOwnerId()});s.location=this.FOLLOW_LOCATION_PHOTO;new i(this.unsubscribeEndpoints[this.type]).setAllowCrossPageTransition(true).setData(s).setMethod('POST').setReadOnly(false).setErrorHandler(h.inform.curry('UnfollowUserFail',s)).send();}});e.exports=q;});
__d("PhotosButtonTooltips",["Arbiter","DOMDimensions","Style","Tooltip"],function(a,b,c,d,e,f){var g=b('Arbiter'),h=b('DOMDimensions'),i=b('Style'),j=b('Tooltip'),k=[],l=[],m;function n(r,s){if(!r||!r.length||!s||!s.length||r.length!=s.length)throw new Error('Incorrect arguments passed in from PHP for photo button cropping');var t=0,u=[],v=false;for(t=0;t<r.length;t++){u.push(h.getElementDimensions(r[t]).width);if(u[t])v=true;}if(v){r.forEach(function(z){i.set(z,'max-width','100%');});for(t=0;t<r.length;t++){var w=r[t],x=u[t];if(x){var y=h.getElementDimensions(w).width;if(y>x){j.set(w,s[t]);l.push(w);}}}r.forEach(function(z){i.set(z,'max-width','');});}return v;}function o(){k.forEach(g.unsubscribe);k=[];l.forEach(j.remove);l=[];}function p(r,s,t){this.arbiterToken=g.subscribe(r,function(){if(n(s,t))this.arbiterToken.unsubscribe();}.bind(this));}var q={init:function(){if(!m)m=g.subscribe('PhotoSnowlift.CLOSE',o);},registerButtonsOnPaging:function(r,s){k.push(new p('PhotoSnowlift.DATA_CHANGE',r,s).arbiterToken);},registerButtonsOnTaggingOn:function(r,s){k.push(new p('PhotoTagger.ACTIVATED_TAGGING',r,s).arbiterToken);},registerButtonsOnTaggingOff:function(r,s){k.push(new p('PhotoTagger.DEACTIVATED_TAGGING',r,s).arbiterToken);}};e.exports=q;});